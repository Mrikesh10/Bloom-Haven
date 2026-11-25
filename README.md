# Bloom Haven – build the Android APK on GitHub

1. Create a free account at github.com and click **New repository** (any name, e.g. `bloom-haven`, Public or Private).
2. On the new repo page click **uploading an existing file**, drag in **everything inside this folder**
   (including the hidden `.github` folder – if your computer hides it, upload the zip contents via GitHub Desktop or
   `git push`), then **Commit changes**.
   The file `.github/workflows/build-apk.yml` MUST end up in the repo.
3. Open the **Actions** tab → **Build Android APK**. It starts automatically (or press **Run workflow**). It takes ~5–8 minutes.
4. When it shows a green tick, open the run and download **BloomHaven-debug-apk** at the bottom (a zip containing `app-debug.apk`).
5. Send `app-debug.apk` to the phone, open it, and allow "Install unknown apps" when asked.

## Updating the game
Replace `www/index.html` (and `www/assets/`) in the repo and commit – a new APK is built automatically.

## Play Store later
The debug APK is for installing on your own phones. The Play Store needs a signed release (`.aab`) – ask and I'll add that workflow.
