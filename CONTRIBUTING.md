
# Contributing to NSMB Central Mod Repository

We welcome all contributors! Follow the steps below to submit your mod:

## Steps to Contribute:

1. **Fork this repository**  
   Click the "Fork" button on the top-right of this repository to create your own copy.

2. **Clone your forked repository**  
   Use this command to clone your fork to your local machine:
   ```bash
   git clone https://github.com/<your-username>/nsmb-mods.git
   ```

3. **Create a new folder for your mod**  
   In the `mods` directory, create a folder named after your mod. For example:
   ```bash
   /mods/my-awesome-mod
   ```

4. **Add a mod page**  
   In your folder, add a `README.md` file using [this template](./mods/example/README.md).

   If you would like to make your page using HTML instead of markdown, add a file named `index.html`.
   
   (Note: `index.html` takes priority over `README.md`)

5. **Commit and push your changes**  
   After adding your mod, commit your changes:
   ```bash
   git add mods/my-awesome-mod
   git commit -m "Added my awesome mod"
   git push origin main
   ```

6. **Submit a Pull Request (PR)**  
   On GitHub, open a Pull Request (PR) from your fork's `main` branch to this repository's `main` branch.

7. **Wait for Admin Review**  
   An admin will review your submission. If approved, your mod will appear on [NSMB Central Mods](https://www.nsmbcentral.net/mods).
