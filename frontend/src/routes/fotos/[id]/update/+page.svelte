<script>
    import {FOTOSTORE} from '../../../../foto-store'
    import {goto} from '$app/navigation'
    import {onMount} from 'svelte'
    let name = '';
    let autor = '';
    let files;
    let showInvalidMessage = false;
    export let data;
    let id;

    let validFields = () => {
        return name.length > 3 && autor.length > 3
    }

    let handleSubmit = () => {
        if (!validFields()){
            showInvalidMessage = true;
            return
        }
        const ENDPOINT = `http://localhost:8000/api/fotos/${id}/`;
        let data = new FormData()
        data.append('name', name)
        data.append('autor', autor)

        if (files) {
            data.append('image', files[0])

        }

        fetch(ENDPOINT, {method: 'PUT', body: data}).then(response => response.json()).then(data =>{
            FOTOSTORE.update(prev => {
                let updateFotos = $FOTOSTORE.slice()
                let index = updateFotos.findIndex(foto => foto.id == data.id)
                updateFotos[index] = data
                return updateFotos
            })
        })

        goto('/fotos/')
    }

    onMount(async function(){
        id = data.id
        let foto = {}
        if ($FOTOSTORE.length){
            foto = $FOTOSTORE.find(foto => foto.id == id)
        } else {
            const ENDPOINT = `http://localhost:8000/api/fotos/${data.id}`;
            let response = await fetch(ENDPOINT);
            if (response.status == 200) {
                foto = await response.json();
            } else {
                foto = null;
            }
        }
        ({name, autor} = foto)
    })
</script>


<div>

    <h2 class="my-4">Actualizar una Foto</h2>

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
