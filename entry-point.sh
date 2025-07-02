#!/bin/bash

# exit on error
set -o errexit

# Colors
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
CYAN="\033[0;36m"
NC="\033[0m" # No Color
RED="\033[0;31m"

SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit
pwd

echo -e  "${CYAN}==> Checking .env ${NC}"
if [ ! -d ".env" ]; then
  echo -e  "${RED}  ==> .env dir not found!${NC}"
  echo -e "${YELLOW}  ==> Creating .env dir...${NC}"
  python3 -m venv .env
  source .env/bin/activate
fi
source .env/bin/activate

echo -e "${CYAN}==> Checking app.env file${NC}"
if [ ! -f "app.env" ]; then
    echo -e "${YELLOW}    app.env file not found!${NC}"
    echo -e "${CYAN}    Creating app.env file...${NC}"
    cp app.example.env app.env
    echo -e "${GREEN}    app.env file created!${NC}"
    echo -e "${YELLOW}    You can add your credentials to  app.env file!${NC}"
else
    echo -e "${GREEN}    app.env file found!${NC}"
fi

echo -e "${CYAN}==> Updating dependencies${NC}"
pip install -r requirements.txt 

cd core || exit

# create tables
echo -e "${CYAN}==> Updating Database Tables${NC}"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py spectacular --file schema.yml
echo -e  "${GREEN}==> The Database has been updated${NC}"

echo -e "${YELLOW}==> Creating superuser...${NC}"

cat create_superuser.py | python3 manage.py shell
# fi
echo -e "${GREEN}==> Starting the Server${NC}"
python3  manage.py runserver

