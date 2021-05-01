function Button({text, onClick, color, id, type}) {
    return (
        <button id={id} onClick={onClick} style={{backgroundColor:color}} className='btn' type={type}>
            {text}
        </button>
    )
}

export default Button