using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string server = $"{PlooConstants.SERVER}Deals";
        string token = $"{PlooConstants.API_KEY}";

        using (HttpClient client = new HttpClient())
        {
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            client.DefaultRequestHeaders.Add("User-Key", token);

            HttpResponseMessage response = await client.GetAsync(server);

            if (response.IsSuccessStatusCode)
            {
                string responseContent = await response.Content.ReadAsStringAsync();
                // Handle the response data here
                // Assuming the response is in JSON format
                // You'll need to parse it using a JSON library

                Console.WriteLine("Response received:");
                Console.WriteLine(responseContent);
                


            }
            else
            {
                // Handle the error here
                Console.WriteLine($"Request failed with status code {response.StatusCode}");
            }
        }
    }
}
