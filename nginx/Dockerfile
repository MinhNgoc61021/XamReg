# Multi-stage means the build context needs to be the same, that's a bit disappointing (coupling!)...
FROM nginx:1.13.9-alpine

COPY nginx/nginx.conf /etc/nginx/nginx.conf

COPY --from=jsbuilder /client/dist/ app/