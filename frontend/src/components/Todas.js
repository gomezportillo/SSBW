// components/Todas.js
import React, { Component } from 'react'
import Peli from './Peli'

export default class Todas extends Component
{
  constructor(props)
  {
    super(props)
    this.state = {          // variable estado de la clase, lista de películas
      pelis: [ {title: 'Si lees esta peli NO estás conectado a la BBDD'} ]
    }
  }

  render()
  {
    // re-renderiza al cambiar el state
    return (
      <div>
      Todas las pelis: <br />
      {this.state.pelis.map(peli => {  // arrow function
        return (
          <Peli peli={peli} />
        )
      })}
      </div>
    )
  }

  // llamada al API
  componentDidMount()
  {
    fetch('https://localhost/ejercicios/api_pelis')  // o el que sea
    .then(res => { return res.json()})
    .then(data => {
      console.log(data)
      this.setState({pelis:data})
    }).catch(error => {
      console.log(error)
    })

  }
}
