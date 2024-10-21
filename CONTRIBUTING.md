
# Contributing to NSMB Central Mod Repository

We welcome all contributors! Follow the steps below to submit your mod:

## Steps to Contribute:

### If you're familiar with git
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

### If you want to use the GitHub website

1. **Fork this repository**  
   Click the "Fork" button on the top-right of this repository to create your own copy. On the following screen, just press "Create fork" at the bottom right.

2. **Add a mod page**   
   At the top of the page, press `Add File -> Create new file`. Now, at the top of the page, type `mods/<your mod name>/README.md` (the slashes will automatically make it a path instead of a file name).

   Now, copy [this template](./mods/example/README.md), and fill out the file from there.

   If you would like to make your page using HTML instead of markdown, name the file `index.html` instead.
   
   (Note: `index.html` takes priority over `README.md`)

3. **Commit your changes** 
   At the top right, press `Commit changes`.

   Change the commit message to your mod name.

   Click `Commit changes` at the bottom.

(Repeat steps 2 & 3 for additional files you need, such as your `.xdelta`. Make sure to upload assets into `/mods/<your mod name>/assets/`)

4. **Submit a pull request (PR)**   
   At the top, press `Contribute`.

   Then, press `Open pull request`.

   Finally, press `Create pull request` at the bottom.

5. **Wait for Admin Review**  
   An admin will review your submission. If approved, your mod will appear on [NSMB Central Mods](https://www.nsmbcentral.net/mods).
