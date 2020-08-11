import React from 'react';
import './App.css';
import axios from'axios'
import Home from './Component/home'

class App extends React.Component{
    state = {
        Selectedfile:null,
        PredictedSign:null,
        previewImage:null
    }

    fileSelectedHandler = event => {
        console.log(event.target.files[0])
        let file = event.target.files[0]
        if (file){
          this.setState({
            Selectedfile: file,
            previewImage: URL.createObjectURL(file)
          })
        }else{
          return
        }
    }

  fileUploadHandler = (e) => {
    const fd = new FormData()
    fd.append('file',this.state.Selectedfile,'download.png')
    axios.post('http://127.0.0.1:5000/predict',fd).
      then(res=>{
        console.log(res.data)
            this.setState({
              PredictedSign: res.data
            })
      })

  }
    render(){
        return(
            <div className='app'>
                <Home fileUploadHandler={this.fileUploadHandler}
                fileSelectedHandler={this.fileSelectedHandler}
                Selectedfile={this.state.Selectedfile}
                previewImage={this.state.previewImage}
                PredictedSign={this.state.PredictedSign}
                />
            </div>
        );
    }
}

export default App;
