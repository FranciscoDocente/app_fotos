<script>
    import {FOTOSTORE} from '../../../foto-store';
    import {onMount} from 'svelte';

    export let data;
    let foto;

    onMount(async function(){
        if ($FOTOSTORE.length){
            foto = $FOTOSTORE.find(foto => foto.id == data.id)
        } else {
            const ENDPOINT = `http://localhost:8000/api/fotos/${data.id}`;
            let response = await fetch(ENDPOINT);
            if (response.status == 200) {
                foto = await response.json();
            } else {
                foto = null;
            }
        }
    })

    
</script>

<div class="row mt-4">
    {#if foto }
        <h2 class="mb-4">{ foto.name }</h2>
        <div class="col-12 col-md-4">
            <img src="{ foto.image }" alt="Foto" class="w-100"/>
        </div>
        <div class="col-12 col-md-8">
            <p class="mb-2"><b>{ foto.name }</b>,<br> autor <i>{ foto.autor }</i></p>

            <a href="/fotos/{foto.id}/update" class="btn btn-primary mt-2">Actualizar</a>
        </div>
    {:else }
        <p>No foto was found with ID {data.id}</p>
    {/if }
</div>