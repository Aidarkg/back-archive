<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Archive of the President</h1>
    <p>This project is a web application for managing and displaying archive the president. The application is built 
using Django and deployed using Docker. Below are the instructions to set up and run the project.</p>
    <h2>Prerequisites</h2>
    <ul>
        <li>Docker</li>
        <li>Docker Compose</li>
    </ul>
    <h2>Setup</h2>
    <ol>
        <li>
            <strong>Clone the repository:</strong>
            <pre><code>git clone https://gitlab.geeks.kg/president-archive/backend-president-archive.git
cd backend-president-archive</code></pre>
        </li>
        <li>
            <strong>Create the <code>.docker.env</code> file:</strong>
            <p>Create a file named <code>.docker.env</code> in the root directory of the project with the following content:</p>
            <pre><code>SECRET_KEY='django-insecure-e$+7o+vwt(rxenih*z+yt(fj^84b#ag%34dj3xgo1&h8btm%rf'
DEBUG='False'

EMAIL_HOST_USER='email@gmail.com'  # replace with your email
EMAIL_HOST_PASSWORD='password'  # replace with your email application password
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'  # replace with your email host if different

REDIS_HOST=redis
REDIS_PORT=6379

POSTGRES_DB=archive
POSTGRES_USER=archive
POSTGRES_PASSWORD=archive
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

PRODUCTION=True</code></pre>
        </li>
        <li>
            <strong>Build and run the Docker containers:</strong>
            <pre><code>docker-compose up --build -d</code></pre>
        </li>
        <li>
            <strong>Access the web container:</strong>
            <p>Once the containers are up and running, access the web container to install Certbot and obtain an SSL certificate.</p>
            <pre><code>docker exec -it web /bin/sh</code></pre>
            <p>Inside the container, run the following commands:</p>
            <pre><code>apt update
apt install certbot python3-certbot-nginx
certbot --nginx</code></pre>
            <p>Follow the prompts to enter your email and domain name to obtain the SSL certificate.</p>
        </li>
    </ol>
    <h2>Additional Notes</h2>
    <ul>
        <li>Ensure that your email host, user, and password are correctly configured in the <code>.docker.env</code> file.</li>
        <li>You may need to adjust the email host if you are not using Yandex.</li>
        <li>The project is configured to run in production mode (<code>PRODUCTION=True</code>), which ensures that debug mode is turned off and other production settings are applied.</li>
    </ul>
    <p>For further customization and settings, refer to the project's documentation and the <code>settings.py</code> file within the Django application.</p>
</body>
</html>
