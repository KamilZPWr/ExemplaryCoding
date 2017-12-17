package com.example.kamil.wisielecv2

import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_give_word.*


class GiveWord : AppCompatActivity(){
    var playerOne:String?=null
    var playerTwo:String?=null
    var activePlayer:Int?=null
    var playerOnePoints:Int?=null
    var playerTwoPoints:Int?=null
    var onePlayer = Player("ktoś")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_give_word)
        confirmBu.setOnClickListener { getUserWord() }

        val bundle:Bundle = intent.extras

        playerOne = bundle.getString("playerOne")
        playerTwo = bundle.getString("playerTwo")
        playerOnePoints = bundle.getInt("playerOnePoints")
        playerTwoPoints = bundle.getInt("playerTwoPoints")
        activePlayer = bundle.getInt("activePlayer")
        

        if (activePlayer==1){
            textView.text="$playerOne please write word!"
        }
        else{
            textView.text="$playerTwo please write word!"
        }
    }

    fun getUserWord(){
        val word = newWord.text.toString()

        if(word.length==0 || word == "your word"){
            Toast.makeText(this,"Please write your word!",Toast.LENGTH_LONG).show()
        }
        else if (word.length>0) {
            val intent = Intent(this, MultiPlayGame::class.java)
            intent.putExtra("playerOne", playerOne)
            intent.putExtra("playerTwo",playerTwo)
            intent.putExtra("word",word)
            intent.putExtra("activePlayer",activePlayer)
            intent.putExtra("playerOnePoints",playerOnePoints)
            intent.putExtra("playerTwoPoints",playerTwoPoints)
            startActivity(intent)}

    }

}

