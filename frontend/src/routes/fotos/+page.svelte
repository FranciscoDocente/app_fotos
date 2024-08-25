<script>
    import {FOTOSTORE} from '../../foto-store';
    import {onMount} from 'svelte';
    
    onMount(async function () {
        if(!$FOTOSTORE.length) {
        const ENDPOINT = 'http://127.0.0.1:8000/api/fotos/';
        const RESPONSE = await fetch(ENDPOINT);
        const DATA = await RESPONSE.json();
        FOTOSTORE.set(DATA);
        }
        
    })

    let handleDelete = (id) => {
        const ENDPOINT = `http://localhost:8000/api/fotos/${id}/`
        fetch(ENDPOINT, {method: 'DELETE'}).then(response => {
            if (response.status == 204) {
                FOTOSTORE.update(prev => prev.filter(foto => foto.id != id))
            }
        })
    }
</script>

<div>
    <h2 class="my-4">Lista de Fotos</h2>
    
    <div class="my-4 row">
        {#each $FOTOSTORE as foto}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover" 
                    src="{foto.image}" 
                    alt="Foto">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="card-title">{ foto.name }</h5>
                        <p class="card-text">Realizado por { foto.autor }</p>
                    </div>
                    <div>
                        <a href="/fotos/{foto.id}" class="btn btn-primary">Ver</a>

                        <button on:click={() => handleDelete(foto.id)} class="btn btn-danger ml-2">
                            Eliminar
                        </button>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>