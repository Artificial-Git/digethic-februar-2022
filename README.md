# python-template

## Visual Studio Code

This repository is optimized for [Visual Studio Code](https://code.visualstudio.com/) which is a great code editor for many languages like Python and Javascript. The [introduction videos](https://code.visualstudio.com/docs/getstarted/introvideos) explain how to work with VS Code. The [Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) provides an introduction about common topics like code editing, linting, debugging and testing in Python. There is also a [Data Science](https://code.visualstudio.com/docs/datascience/overview) section showing how to work with Jupyter Notebooks and common Machine Learning libraries.

The `.vscode` directory contains configurations for useful extensions like [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens0) and [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python). When opening the repository, VS Code will open a prompt to install the recommended extensions.

## Development Setup

Open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal) and run the setup script for your OS. This will install a [Python virtual environment](https://docs.python.org/3/library/venv.html) with all packages specified in `requirements.txt`.

If everything works you should be able to activate the Python environment by entering `source .venv/bin/activate` in the terminal. The command `python src/hello.py` will print the text "hello world" to your terminal.

### Linux and Mac Users

- run the setup script `./setup.sh` or `sh setup.sh`

### Windows Users

- run the setup script `.\setup.ps1`

## Development

- Mac/Linux: activate python environment: `source .venv/bin/activate`
- Windows: activate python environment: `.\.venv\Scripts\Activate.ps1`
- run python script: `python <srcfilename.py> `, e.g. `python train.py`
- install new dependency: `pip install scikit-learn`
- save current installed dependencies back to requirements.txt: `pip freeze > requirements.txt`

## Troubleshooting

If something with your python version is not working, you might need to change the first line in `setup.sh` or `setup.ps1`
from

```
python3 -m venv .venv
```

to

```
python -m venv .venv
```

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.tsx`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.tsx`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check  out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

Deploy this project: [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/git/external?repository-url=https%3A%2F%2Fgithub.com%2FOFranke%2Fbaummethoden-frontend&env=NEXT_PUBLIC_PREDICTION_API)

## Used Technology

- React: https://reactjs.org/
- React Framework: https://nextjs.org/
- Hosting: https://vercel.com/

# Python ist sehr cühl.
