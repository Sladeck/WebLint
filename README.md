# WebLint Project in Python

> This project is a school project in python language.



Développez un programme en Python 3.6 ou 3.7, s'utilisant dans un shell uniquement (pas d'interface graphique, pas d'interface web, pas de curses, que du text dans un émulateur de terminal) prenant une (ou plusieurs) URL en paramètre et effectuant une batterie de tests dessus, l'idée est de pouvoir l'utiliser dans une CI comme un jslint, csslint, des tests unitaires, etc... ou comme outil de monitoring branché sur un nagios like.

Le projet s'appelle [weblint](https://mdk.fr/pages/obiree2uaza2sh-rendu.html).

Les tests à implémenter sont libres, le nombre de tests, la variété des tests, et la qualité de l'implémentation feront partie de la note.

Voici quelques idées de tests pour vous inspirer :

- Cohérence des headers (encoding pareil que dans la meta et que dans la page, content type existant) (langue du contenu identique à la langue annoncée,...), Vérifier que la page est bien envoyée compressée si le client le gère, ...
- Headers à jour : CSP, x-frame-options etc...
- Vérification orthographique
- Vérification grammaticales
- Temps de réponse
- Présence de 404
- Présence de liens HTTP alors qu'en face y'a du HTTPS
- Si présence de flux RSS / Atom : vérifier leur contenu, content types, ...
- Si présence de CSS / JS externes vérification de leur headers, temps de réponse, contenu, minification
- Si c'est une Home page, vérifier aussi le robots.txt, le security.txt, ...
- Si c'est du HTTPS vérifier aussi si c'est bien fait (expiration pas trop proche,...)
- Si y'a du AMP vérifier via amphtml-validator

Les erreurs devront être remontées dans un format simple et lisible, une erreur par ligne, aucune ligne ne doit être autre chose qu'une erreur, inspirez vous de pylint, flake8, gcc, php -l. Vous pouvez implémenter une option "--verbose" pour rajouter des informations, éventuellement "-vv" pour rajouter du débug (n'hésitez pas à utiliser les bibliothèque standard logging et argparse).
