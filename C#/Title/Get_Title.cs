using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

class Program
{
    static async Task Main(string[] args)
    {
        string server = $"{PlooConstants.SERVER}Deals";
        string token = $"{PlooConstants.API_KEY}";
        var quantity = 0;
        using (HttpClient client = new HttpClient())
        {
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            client.DefaultRequestHeaders.Add("User-Key", token);

            HttpResponseMessage response = await client.GetAsync(server);

            if (response.IsSuccessStatusCode)
            {
                string responseContent = await response.Content.ReadAsStringAsync();

                // Deserialize the JSON response
                var data = JObject.Parse(responseContent);

                if (data["value"] != null)
                {
                    foreach (var item in data["value"])
                    {
                        string title = item["Title"].ToString();
                        quantity++;
                        Console.WriteLine(title);
                    }
                }
            }
            else
            {
                // Handle the error here
                Console.WriteLine($"Request failed with status code {response.StatusCode}");
            }
        }

                Console.WriteLine($"Number of deals: {quantity}");
    }
}
