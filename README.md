HOW TO LOAD THE PROJECT

1. CLONE REPOSITORY TO THE DESIRED PATH ON YOUR MACHINE WITH:
git clone https://github.com/firtaltv/massage.git

2. ADD .env FILE WITH FOLLOWING CONFIGURATIONS:
- POSTGRES_HOST=<YOUR_DB_HOST>
- POSTGRES_PORT=<YOUR_DB_PORT>
- POSTGRES_DB=<YOUR_DB>
- POSTGRES_USER=<YOUR_DB_USER>
- POSTGRES_PASSWORD=<YOUR_DB_PASSWORD>
- SECRET_KEY=<YOUR_SECRET_KEY>
- DEBUG= SET True ONLY for development purposes on local machine

3. BUILD AND RUN THE PROJECT:
sudo docker-compose up --build

4. SIGN UP TO ADMIN PANEL AT:

127.0.0.1:8000/admin

WITH THE FOLLOWING CREDENTIALS:

login: admin
password: admin
