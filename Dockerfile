FROM node:20
WORKDIR /var/www/html
COPY . .
RUN npm install express
EXPOSE 82
CMD ["node","server.js"]