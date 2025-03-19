# Bibliotecas
* colorama==0.4.6
* coverage==7.7.0
* iniconfig==2.0.0
* packaging==24.2
* pluggy==1.5.0
* pytest==8.3.5
* pytest-cov==6.0.0

********************************
## Comandos
pytest:
* pytest -verbonse ou -v
* pytest -v -m calcular_bonus

pytest-cov:
* pytest --cov
* pytest --cov=codigo tests/

 No pytest-cov, podemos usar a tag --cov-report term-missing para especificar outro tipo de relatório, que exibirá os termos faltantes para os 100% de cobertura.

 * pytest --cov=codigo tests/ --cov-report term-missing
 * pytest --cov=codigo tests/ --cov-report html:tests/reports/bytebank

 Por fim, vamos aprender como gerar relatórios em formato XML, um padrão do mercado, estabelecido em diversas linguagens de programação e bastante útil para enviar a outras pessoas.

 * pytest --junitxml report.xml

 De forma complementar, podemos gerar um relatório do coverage, executando o comando

 * pytest --cov-report xml

********************************