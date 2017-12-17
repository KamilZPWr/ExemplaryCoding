package com.example.kamil.wisielecv2

import android.content.Context
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {

    var gameType:Int?=null
    var context: Context?=null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun startGame(view:View){
        var buSelected = view as Button

        when(buSelected.id){
            R.id.onePlayerBu -> {
                val intent = Intent(this,PlayGame::class.java)

                if(firstPlayerName.text.toString()=="Enter name"){
                    intent.putExtra("playerOne","First player")
                }else{
                    intent.putExtra("playerOne",firstPlayerName.text.toString())
                }
                startActivity(intent)
            }

            R.id.twoPlayerBu -> {
                val intent = Intent(this,GiveWord::class.java)
                if(firstPlayerName.text.toString()=="Enter name"){
                    intent.putExtra("playerOne","First player")
                }else{
                    intent.putExtra("playerOne",firstPlayerName.text.toString())
                }
                if(secondPlayerName.text.toString()=="Enter name"){
                    intent.putExtra("playerTwo","Second player")
                }else{
                    intent.putExtra("playerTwo",secondPlayerName.text.toString())
                }
                intent.putExtra("activePlayer",1)
                intent.putExtra("playerOnePoints",0)
                intent.putExtra("playerTwoPoints",0)
                startActivity(intent)
            }
        }

    }
}
