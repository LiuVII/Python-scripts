rm -rf ~/Library/Application\ Support/Flux
rm -rf ~/Library/Containers/com.justgetflux.flux
mkdir /tmp/Flux 2> /dev/null
mkdir /tmp/com.justgetflux.flux 2> /dev/null
ln -s /tmp/Flux ~/Library/Application\ Support/Flux
ln -s /tmp/com.justgetflux.flux ~/Library/Containers/com.justgetflux.flux
