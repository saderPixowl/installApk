package com.pixowl.resetdevicesettings;

import android.content.Context;
import android.net.wifi.WifiConfiguration;
import android.net.wifi.WifiManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        wifi();
        TextView tv = findViewById(R.id.textLabel);
        tv.setText("Ok");
    }







    //tested on android 4.4 and 8
    void wifi()
    {
        try {

            WifiManager wifi = (WifiManager)
                    getApplicationContext().getSystemService(Context.WIFI_SERVICE);

//            WifiConfiguration wc = new WifiConfiguration();
//            wc.SSID = "\"devpixowl\"";
//            wc.preSharedKey  = "\"338pixowl\"";
//            wc.hiddenSSID = true;
//            wc.status = WifiConfiguration.Status.ENABLED;
//
//            wc.allowedGroupCiphers.set(WifiConfiguration.GroupCipher.TKIP);
//            wc.allowedGroupCiphers.set(WifiConfiguration.GroupCipher.CCMP);
//            wc.allowedKeyManagement.set(WifiConfiguration.KeyMgmt.WPA_PSK);
//
//            wc.allowedPairwiseCiphers
//                    .set(WifiConfiguration.PairwiseCipher.TKIP);
//            wc.allowedPairwiseCiphers
//                    .set(WifiConfiguration.PairwiseCipher.CCMP);
//            wc.allowedProtocols.set(WifiConfiguration.Protocol.RSN);

            if (!wifi.isWifiEnabled())
                wifi.setWifiEnabled(true);


        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
