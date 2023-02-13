# trame-formkit

This directory capture the steps to enable FormKit into trame-formkit.

## Update FormKit

```bash
export SRC_URL=https://cdn.jsdelivr.net/npm/
export DST_PATH=../trame_formkit/module/serve
export VERSION=@formkit/vue@1.0.0-beta.15

mkdir -p $DST_PATH

curl $SRC_URL/$VERSION/dist/formkit-vue.js -Lo $DST_PATH/formkit.js
```
