
all: compte_rendu

compte_rendu:
	pandoc compte_rendu.md --pdf-engine=xelatex -o compte_rendu.pdf -f markdown -t latex


