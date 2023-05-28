<script lang="ts">
    let selectedFiles: FileList;
    
    const apiUrl = 'http://localhost:8000/api/';
    const url: string = apiUrl + "upload";

    let status: string = "";

    async function handleFileUpload() {
        console.log("uploading file")
        status = "Uploading file...\n";
        let uploadData = new FormData();
        uploadData.append('file', selectedFiles[0]);

        let serverResponse = await fetch(url, {
            method: 'POST',
            body: uploadData
        });

        let uploadResult = await serverResponse.json();

        const eventStream = new EventSource(apiUrl + 'status/' + uploadResult.id);
        eventStream.onmessage = (event) => {
            status += event.data + "\n";
            console.log(event.data);
            if (event.data !== "processing") {
                eventStream.close();
                if (event.data === "done") {
                    status += "Upload successful";
                } else {
                    status += "Upload failed";
            }
            }
        }
        console.log(uploadResult);
    }
</script>

<form on:submit|preventDefault={handleFileUpload}>
    <input type='file' bind:files={selectedFiles} />
    <button type='submit'>Upload</button>
</form>

<pre>{status}</pre>

