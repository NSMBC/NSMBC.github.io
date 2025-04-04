# Contributing to NSMB Central Mod Repository

We welcome all contributors to the NSMB Central Mod Repository! This guide will help you submit your mod successfully.

## Table of Contents
- [Submission Methods](#submission-methods)
  - [Using Git (Recommended)](#using-git-recommended)
  - [Using GitHub Website](#using-github-website)
- [Mod Submission Requirements](#mod-submission-requirements)
- [Mod Page Guidelines](#mod-page-guidelines)
- [Review Process](#review-process)
- [Troubleshooting](#troubleshooting)

## Submission Methods

### Using Git (Recommended)

This method is recommended for users familiar with Git and provides more control over your submission.

1. **Fork this repository**  
   Click the "Fork" button on the top-right of this repository to create your own copy.

2. **Clone your forked repository**  
   Use this command to clone your fork to your local machine:
   ```bash
   git clone https://github.com/<your-username>/nsmb-mods.git
   cd nsmb-mods
   ```

3. **Create a new folder for your mod**  
   In the `mods` directory, create a folder named after your mod. For example:
   ```bash
   mkdir -p mods/my-awesome-mod
   ```

4. **Add your mod files**  
   - Create a `README.md` file using [this template](./mods/example/README.md)
   - Add your mod files (`.xdelta`, etc.) to the folder
   - Create an `assets` folder for images and other media:
     ```bash
     mkdir -p mods/my-awesome-mod/assets
     ```

5. **Commit and push your changes**  
   ```bash
   git add mods/my-awesome-mod
   git commit -m "Added my awesome mod"
   git push origin main
   ```

6. **Submit a Pull Request (PR)**  
   - Go to your fork on GitHub
   - Click "Compare & pull request"
   - Fill in the PR description with details about your mod
   - Click "Create pull request"

### Using GitHub Website

This method is suitable for users who prefer a web-based approach.

1. **Fork this repository**  
   Click the "Fork" button on the top-right of this repository, then press "Create fork" at the bottom right.

2. **Add a mod page**   
   - Click `Add File -> Create new file`
   - Type `mods/<your mod name>/README.md` in the file name field
   - Copy [this template](./mods/example/README.md) and fill it out
   - Click "Commit changes" at the bottom

3. **Add mod files and assets**
   - Repeat the file creation process for your mod files
   - For assets, create a folder first:
     - Click `Add File -> Create new file`
     - Type `mods/<your mod name>/assets/.gitkeep` (this creates the folder)
     - Then add your image files to this folder

4. **Submit a pull request (PR)**   
   - Click "Contribute" at the top
   - Select "Open pull request"
   - Fill in the PR description
   - Click "Create pull request"

## Mod Submission Requirements

Your mod submission must include:

- A descriptive name for your mod folder
- Either a `README.md` or `index.html` file (see [Mod Page Guidelines](#mod-page-guidelines))
- Your mod files (`.xdelta` or other patch formats)
- At least one screenshot or preview image in the `assets` folder

## Mod Page Guidelines

### README.md vs index.html

- **README.md**: A simple to make page for your mod
- **index.html**: More flexible, allows for custom styling and layout
- **Priority**: If both files exist, `index.html` will be used

### Content Requirements

Your mod page should include:

1. **Title**: The name of your mod
2. **Description**: A brief description of your mod
3. **Screenshots**: At least one image showing your mod in action
4. **Download Link**: A link to your `.xdelta`. This file should be in `mods/<your mod name>/assets/`.
5. **Credits**: Any resources or inspirations used

### Best Practices

- Use clear, descriptive language
- Include high-quality screenshots
- Test all links before submission
- Follow the template structure for consistency

## Review Process

1. **Initial Check**: An automated check ensures your submission meets basic requirements
2. **Admin Review**: A repository admin will review your submission
3. **Feedback**: If changes are needed, you'll receive comments on your PR
4. **Approval**: Once approved, your mod will be merged and appear on [NSMB Central Mods](https://www.nsmbcentral.net/mods)

## Troubleshooting

### Common Issues

- **PR Validation Failed**: Ensure your mod folder contains either a `README.md` or `index.html` file
- **Missing Assets**: Make sure your images are in the `assets` folder
- **Broken Links**: Test all links in your mod page before submission

### Need Help?

If you encounter issues not covered here, please:
1. Check the [Issues](https://github.com/your-username/nsmb-mods/issues) page
2. Open a new issue with a detailed description of your problem
3. Tag your issue with the "help wanted" label

---

Thank you for contributing to the NSMB Central Mod Repository!
