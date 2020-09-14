FROM node:12.2.0-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install
ENV PATH /app/node_modules/.bin:$PATH

COPY . ./

# start app
CMD ["npm", "start"]