function Entry({entry}) {
    return (
        <div className='entry'>
            <p><strong>{entry.tool}</strong> {entry.detail}</p>
        </div>
    )
}

export default Entry
