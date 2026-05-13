from src.api_service import buscar_medicamento


def test_buscar_medicamento():
    resultado = buscar_medicamento("aspirin")

    assert resultado is not None