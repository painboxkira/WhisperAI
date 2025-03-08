# YouTube Audio Transcriber 🎤📄

Ce projet Python propose une démonstration technique simple et intuitive permettant de télécharger et transcrire automatiquement l'audio des vidéos YouTube en utilisant l'API Whisper d'OpenAI.

---

## 🚀 Fonctionnalités

- Téléchargement automatique du meilleur format audio disponible depuis YouTube.
- Génération automatique de noms de fichiers sécurisés.
- Transcription audio rapide et précise grâce à l'API Whisper d'OpenAI.
- Interface graphique intuitive pour une expérience utilisateur fluide.

---

## 📦 Bibliothèques requises

Installez les dépendances nécessaires avec la commande suivante :

```bash
pip install openai yt-dlp tkinter || winget install ffmpeg
```

---

## 🔑 Configuration de la clé API OpenAI

1. Rendez-vous sur [platform.openai.com](https://platform.openai.com/api-keys).
2. Connectez-vous ou créez un compte.
3. Générez une nouvelle clé API.
4. Définissez votre clé API dans votre environnement :

```bash
set OPENAI_API_KEY=votre-cle-api
```

---

## ▶️ Exécution du programme

Après avoir configuré votre clé API, lancez le script depuis votre terminal :

```bash
python votre_script.py
```

Entrez l'URL YouTube et sélectionnez les options de début et de fin optionnelles directement depuis l'interface graphique.

---

## 📁 Structure du projet

- Téléchargements audio sauvegardés au format `.webm`
- Transcriptions sauvegardées au format `.txt`

---

## 🛠️ Technologies utilisées

- Python
- yt-dlp
- API OpenAI Whisper
- Tkinter pour l'interface graphique

---

Profitez dès maintenant de cet outil simple et efficace pour transformer vos vidéos YouTube préférées en textes exploitables facilement !

