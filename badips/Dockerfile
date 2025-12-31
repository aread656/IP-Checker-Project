FROM node:20
WORKDIR /var/www/html
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 82
CMD ["node","server.js"]