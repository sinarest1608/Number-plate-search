import 'package:flutter/material.dart';



void main() => runApp(new MyApp());



//WILL NOT CHANGE

class MyApp extends StatefulWidget {

  @override
  _MyAppState createState() => new _MyAppState();
}


class _MyAppState extends State<MyApp> {

  String _title = "hello";
  String _mystate = "No State";




  void _onpressed(String message){

    setState((){ _mystate = message;});

print(message);
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return new MaterialApp(
      title: "State Check",
      home: new Scaffold(
        appBar: AppBar(
          title: new Text(_title),
          actions: <Widget>[
            new IconButton(icon:new Icon(Icons.account_balance), onPressed: (){ _onpressed("Account Balance");}),
            new IconButton(icon:new Icon(Icons.add_alarm), onPressed:(){ _onpressed("Alarmed");}),
            new IconButton(icon:new Icon(Icons.accessibility), onPressed: (){_onpressed("people");}),
            new RaisedButton(child: new Icon(Icons.add_a_photo),onPressed: (){_onpressed("button worked");})
          ],

        ),
        body: new Container(
          padding: const EdgeInsets.all(32.0),
          child: new Center(
            child: new Text(_mystate),
          )
        ),
      ),
    );
  }

}

