# This image will contain the JS code as well since it's nginx serving it.
# Using multi-stage docker build for a smaller final image.
FROM node:lts AS jsbuilder

WORKDIR ./client
COPY . .

RUN npm install

# Multi-stage means the build context needs to be the same, that's a bit disappointing (coupling!)...
FROM nginx:1.13.9-alpine
WORKDIR ./nginx
COPY --from=jsbuilder /client/dist/ app/
COPY /nginx/nginx.conf /etc/nginx/nginx.conf

