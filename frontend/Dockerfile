FROM node:19-alpine
WORKDIR /app
COPY ./package*.json .
COPY ./yarn.lock .
COPY . .
RUN yarn install && yarn cache clean
RUN npm rebuild esbuild
EXPOSE 3000
CMD yarn dev
