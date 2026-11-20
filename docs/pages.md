# Publiczne GitHub Pages DERA-HRI

Jedynym źródłem witryny jest `pages/`; `docs/` przechowuje wewnętrzne instrukcje i dokumentację techniczną. `mkdocs.yml` wymaga `docs_dir: pages`, a `config/pages-policy.json` wymienia każdy plik publiczny. Żaden skrypt nie może kopiować całego repozytorium do witryny.

Na stronie nie wolno publikować instrukcji dla agentów, promptów, komentarzy redakcyjnych, poleceń do autora, instrukcji współtworzenia repozytorium, sekretów ani danych uczestników. Publiczne teksty naukowe mają wyraźnie rozdzielać hipotezę, plan i potwierdzony wynik.

W workflow build i testy działają na zmianach, **publikacja jest wyłącznie ręczna** przez uprawnione uruchomienie `workflow_dispatch` dla `main`. Tryb `Deploy from a branch` z `main:/docs` lub korzenia jest zabroniony. Repo prywatne nie gwarantuje prywatności witryny. Przed uruchomieniem publikacji należy zweryfikować jej rzeczywistą widoczność, prawa, wszystkie grafiki i metadane, zbudowany HTML oraz niezależny przegląd treści.

`python scripts/validate_pages.py` jest statyczną bramką minimalną, nie audytem prawnym ani zgodą na publikację.
