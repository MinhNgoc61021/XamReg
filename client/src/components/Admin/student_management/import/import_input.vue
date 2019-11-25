<template>
    <b-tabs type="is-toggle" expanded>
        <b-tab-item label="Nhập bằng Excel" style="margin: auto">
          <div style="margin: auto;">
            <keep-alive>
              <component v-bind:is="upload"/>
            </keep-alive>
          </div>
        </b-tab-item>
        <b-tab-item label="Nhập bằng tay" >
          <keep-alive>
            <component v-bind:is="input"/>
          </keep-alive>
        </b-tab-item>
    </b-tabs>
</template>
<script>
    import upload from './upload';
    import input from './input';

    export default {
        name: "import",
        components: {
          upload, input
        },
        data() {
            return {
              upload, input
            }
        }
    }
</script>

<style scoped>

</style>
