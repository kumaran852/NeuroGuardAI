import android.app.Service
import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.content.Intent
import android.os.IBinder
import android.util.Log

class ClipboardMonitoringService : Service() {
    private lateinit var clipboard: ClipboardManager

    override fun onCreate() {
        super.onCreate()
        clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
        clipboard.addPrimaryClipChangedListener { handleClipboardChange() }
        Log.d("ClipboardMonitoringService", "Service Created")
    }

    private fun handleClipboardChange() {
        val clipData: ClipData? = clipboard.primaryClip
        if (clipData != null && clipData.itemCount > 0) {
            val text = clipData.getItemAt(0).coerceToText(this).toString()
            Log.d("ClipboardMonitoringService", "Clipboard changed: $text")
            // Additional processing can go here
        }
    }

    override fun onBind(intent: Intent?): IBinder? {
        return null
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("ClipboardMonitoringService", "Service Destroyed")
    }
}