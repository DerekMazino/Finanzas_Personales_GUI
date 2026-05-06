import pytest
from unittest.mock import MagicMock
from src.services.concepto_service import ConceptoService

@pytest.fixture
def mock_deps():
    periodo_service = MagicMock()
    concepto_repo = MagicMock()
    return periodo_service, concepto_repo

def test_validar_datos_nombre_invalido(mock_deps):
    ps, cr = mock_deps
    service = ConceptoService(cr, ps)
    
    with pytest.raises(ValueError, match="El nombre debe comenzar con una letra"):
        service.validar_datos("123 Ingreso", 100, "ingreso")

def test_validar_datos_valor_invalido(mock_deps):
    ps, cr = mock_deps
    service = ConceptoService(cr, ps)
    
    with pytest.raises(ValueError, match="El valor debe ser un número positivo"):
        service.validar_datos("Sueldo", -50, "ingreso")

def test_agregar_concepto_exitoso(mock_deps):
    ps, cr = mock_deps
    service = ConceptoService(cr, ps)
    
    # Simular periodo existente
    ps.verificar_existencia.return_value = True
    ps.periodo_repo.get_by_mes_anio.return_value = (1, 5, 2026)
    cr.create.return_value = 100

    nuevo_id = service.agregar_concepto(5, 2026, "Sueldo", 1500, "ingreso")
    
    assert nuevo_id == 100
    cr.create.assert_called_once()
    # No debería llamar a crear_periodo
    ps.crear_periodo.assert_not_called()

def test_agregar_concepto_recurrente_crea_plantilla(mock_deps):
    ps, cr = mock_deps
    service = ConceptoService(cr, ps)
    
    ps.verificar_existencia.return_value = True
    ps.periodo_repo.get_by_mes_anio.return_value = (1, 5, 2026)
    
    service.agregar_concepto(5, 2026, "Renta", 500, "egreso", es_recurrente=True)
    
    # Debe insertar en conceptos y en plantillas
    assert cr.create.called
    assert cr.db.execute_query.called
    args = cr.db.execute_query.call_args[0]
    assert "plantillas_recurrentes" in args[0]
    assert "Renta" in args[1]

def test_obtener_conceptos_por_periodo(mock_deps):
    ps, cr = mock_deps
    service = ConceptoService(cr, ps)
    
    # Simular periodo existente (id=10)
    ps.periodo_repo.get_by_date.return_value = (10, 5, 2026)
    
    # Simular retorno del repositorio
    cr.get_by_periodo.return_value = [
        (1, 10, "Sueldo", 1500, "ingreso", 0),
        (2, 10, "Renta", 500, "egreso", 1)
    ]
    
    conceptos = service.obtener_conceptos_por_periodo(5, 2026)
    
    assert len(conceptos) == 2
    assert conceptos[0][2] == "Sueldo"
    assert conceptos[1][4] == "egreso"
    cr.get_by_periodo.assert_called_with(10)
