<script>
    import {FOTOSTORE} from '../../../foto-store'
    import {goto} from '$app/navigation'
    let name = '';
    let autor = '';
    let files;
    let showInvalidMessage = false;

    let validFields = () => {
        return name.length > 3 && autor.length > 3
    }

    let handleSubmit = () => {
        if (!validFields()){
            showInvalidMessage = true;
            return
        }
        const ENDPOINT = `http://localhost:8000/api/fotos/`;
        let data = new FormData()
        data.append('name', name)
        data.append('autor', autor)
        data.append('image', files[0])

        fetch(ENDPOINT, {method: 'POST', body: data}).then(response => response.json()).then(data =>{
            FOTOSTORE.update(prev => [...prev, data])
        })

        goto('/fotos/')
    }    
</script>


<div>

    <h2 class="my-4">Añadir una Foto</h2>

    {#if showInvalidMessage}
        <h4 class="text-danger">Los datos del formulario no son validos</h4>
    {/if}

    <div class="col-12 col-md-6">
        <form on:submit|preventDefault={handleSubmit}>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="name" bind:value={name}/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="autor" bind:value={autor}/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="file" bind:files/>
            </div>
        
            <button class="btn btn-primary" type="submit">Enviar</button>
        </form>
    </div>

</div>
