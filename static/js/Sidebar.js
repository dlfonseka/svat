import Entry from './Entry.js'

function Sidebar({log}) {
    return (
        <div> 
        <br/>
        <h2>Annotation Log</h2>
            {log.map((entry) => (<Entry entry={entry}/>))}
        </div>
    )
}

export default Sidebar
