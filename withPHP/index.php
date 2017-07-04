<?php
# cloudVisionDemo.php

// APIキー
$api_key = "AIzaSyCRj9daB-6dv2sW4jTDkrwi0BKxv81UV6Q" ;

// 画像へのパス
$image_path = $_GET["url"]."&token=".$_GET["token"];
$replaceText = str_replace("images/", "images%2F",$image_path);
// Feature Type
$feature = "FACE_DETECTION";

// パラメータ設定
$param = array("requests" => array());
$item["image"] = array("content" => base64_encode(file_get_contents($replaceText)));
$item["features"] = array(array("type" => $feature, "maxResults" => 3));
$param["requests"][] = $item;

// リクエスト用のJSONを作成
$json = json_encode($param);



// リクエストを実行
$curl = curl_init() ;
curl_setopt($curl, CURLOPT_URL, "https://vision.googleapis.com/v1/images:annotate?key=" . $api_key);
curl_setopt($curl, CURLOPT_HEADER, true);
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($curl, CURLOPT_HTTPHEADER, array("Content-Type: application/json"));
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_TIMEOUT, 15);
curl_setopt($curl, CURLOPT_POSTFIELDS, $json);
$res1 = curl_exec($curl);
$res2 = curl_getinfo($curl);
// 取得したデータ
$json = substr($res1, $res2["header_size"]);
$array = json_decode($json, true);

    
    $url = "https://laugh-2dc9f.firebaseio.com/users/data.json";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);      
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");                         
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: text/plain'));
    $jsonResponse = curl_exec($ch);
    $number = json_decode($jsonResponse,true);
    if(curl_errno($ch))
    {
        echo 'Curl error: ' . curl_error($ch);
    }
    curl_close($ch);
    
  
    $face_datas = array("VERY_LIKELY"=>"50","LIKELY"=>"40","POSSIBLE"=>"30","UNLIKELY"=>"20","VERY_UNLIKELY"=>"10","UKNOWN"=>"0");
    
    $sum = $number["body"] + $face_datas[$array["responses"][0]["faceAnnotations"][0]["joyLikelihood"]];
    $data = '{"body": '.$sum.'}';
    $url = "https://laugh-2dc9f.firebaseio.com/users/data.json";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);      
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PATCH");                         
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: text/plain'));
    $jsonResponse = curl_exec($ch);
    if(curl_errno($ch))
    {
        echo 'Curl error: ' . curl_error($ch);
    }
    curl_close($ch);
    
    echo $sum;
