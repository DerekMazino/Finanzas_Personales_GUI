import pytest
from unittest.mock import MagicMock
from src.services.periodo_service import PeriodoService

@pytest.fixture
def mock_repos():
    periodo_repo = MagicMock()
    concepto_repo = MagicMock()
    return periodo_repo, concepto_repo

def test_verificar_existencia_retorna_true_si_existe(mock_repos):
    periodo_repo, concepto_repo = mock_repos
    periodo_repo.get_by_date.return_value = (1, 5, 2026)
    
    service = PeriodoService(periodo_repo, concepto_repo)
    assert service.verificar_existencia(5, 2026) is True

def test_crear_periodo_lanza_error_si_ya_existe(mock_repos):
    periodo_repo, concepto_repo = mock_repos
    periodo_repo.get_by_date.return_value = (1, 5, 2026)
    
    service = PeriodoService(periodo_repo, concepto_repo)
    with pytest.raises(ValueError, match="ya existe"):
        service.crear_periodo(5, 2026)

def test_crear_periodo_exitoso_y_llama_a_copia_recurrentes(mock_repos):
    periodo_repo, concepto_repo = mock_repos
    # Simular que no existe inicialmente
    periodo_repo.get_by_date.side_effect = [None, (2, 6, 2026)]
    # Simular periodos existentes para la lógica de copia (nuevo + anterior)
    periodo_repo.get_all.return_value = [(2, 6, 2026), (1, 5, 2026)]
    # Simular un concepto recurrente en el periodo anterior
    concepto_repo.get_recurrentes_last_period.return_value = [(10, 1, "Sueldo", 1000.0, "ingreso", 1, "")]

    service = PeriodoService(periodo_repo, concepto_repo)
    service.crear_periodo(6, 2026)

    periodo_repo.create.assert_called_once_with(6, 2026)
    concepto_repo.create.assert_called_once() # Se llamó para copiar el sueldo
