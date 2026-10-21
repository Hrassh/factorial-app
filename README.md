# factorial-app

Застосунок для обчислення факторіалу числа з автоматичним тестуванням у GitHub Actions.

## Використання

```
python -m factorial_app 5
120
```

## Тести

```
pip install -r requirements-dev.txt
pytest -v --cov=factorial_app
```

## CI

Workflow `.github/workflows/tests.yml` запускає тести при кожному push
на Python 3.10–3.13.

Локальний запуск через [act](https://github.com/nektos/act):

```
act push
```
