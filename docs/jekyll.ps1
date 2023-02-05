# using the official Jekyll image, see https://github.com/envygeeks/jekyll-docker
# runs on port 4000


# mkdir -p ".bundles_cache"
New-Item -ItemType Directory -Path ".bundles_cache" -Force
docker run `
  --name cis1051-site --rm `
  -v "${PWD}:/srv/jekyll" `
  -e BUNDLE_PATH="/srv/jekyll/.bundles_cache" `
  -p 4000:4000 `
  jekyll/builder:3.8 `
  bash -c "gem install bundler && bundle install && bundle exec Jekyll serve --host 0.0.0.0 --verbose --config _config.yml,_config_dev.yml --no-watch"