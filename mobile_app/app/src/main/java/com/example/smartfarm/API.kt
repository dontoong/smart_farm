package com.example.smartfarm

import retrofit2.Call
import retrofit2.http.*

data class ResponseDC(var result:String? = null)

interface API {
    @GET("http://175.126.123.217:5657/machbase?q=select value from tag where name ='temp' order by time desc limit 1")
    fun getRequest(): Call<ResponseDC>

}