<script lang="ts">
    let selectedFiles: FileList;

    export const url: string = "http://localhost:8000/api/upload";

    async function handleFileUpload() {
        let uploadData = new FormData();
        uploadData.append('file', selectedFiles[0]);

        let serverResponse = await fetch(url, {
            method: 'POST',
            body: uploadData
        });

        let uploadResult = await serverResponse.json();
        console.log(uploadResult);
    }
</script>

<form on:submit|preventDefault={handleFileUpload}>
    <input type='file' bind:files={selectedFiles} />
    <button type='submit'>Upload</button>
</form>
