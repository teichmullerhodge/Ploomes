using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace YourNamespace
{
    class Program
    {
        static async Task Main()
        {
            string PLOOMES_SERVER = Plooconstants.SERVER;
            string PLOOMES_TOKEN = Plooconstants.API_KEY;
            string APP_SERVER = "https://app.com/api/resources"; // Exemplo aleatório
            string APP_TOKEN_AUTH = "<PRIVATE KEY>";

            // Exemplo de chamada para obter dados
            await GetDataByEndpointAsync(PLOOMES_SERVER, PLOOMES_TOKEN, APP_SERVER, APP_TOKEN_AUTH);
        }

        static async Task GetDataByEndpointAsync(string ploomesServer, string ploomesToken, string appServer, string appTokenAuth)
        {
            string endpoint = "your_endpoint_here";
            string top = "10";
            string skip = "0";
            string select = "your_select_here";
            string expand = "your_expand_here";
            string filter = "your_filter_here";
            string orderby = "your_orderby_here";

            using (HttpClient client = new HttpClient())
            {
                client.BaseAddress = new Uri(ploomesServer);
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ploomesToken);
                client.DefaultRequestHeaders.Add("User-Key", ploomesToken);
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

                string url = $"{endpoint}?";

                if (!string.IsNullOrEmpty(top)) url += $"$top={top}&";
                if (!string.IsNullOrEmpty(skip)) url += $"$skip={skip}&";
                if (!string.IsNullOrEmpty(select)) url += $"$select={select}&";
                if (!string.IsNullOrEmpty(expand)) url += $"$expand={expand}&";
                if (!string.IsNullOrEmpty(filter)) url += $"$filter={filter}&";
                if (!string.IsNullOrEmpty(orderby)) url += $"$orderby={orderby}&";

                HttpResponseMessage response = await client.GetAsync(url);

                if (response.IsSuccessStatusCode)
                {
                    string data = await response.Content.ReadAsStringAsync();

                    // Manipule os dados JSON da forma desejada antes de enviá-los para a próxima plataforma
                    // Insira condicionais, por exemplo, envie dados apenas se o valor não estiver vazio

                    await PostDataToAppAsync(data, appServer, appTokenAuth);

                    // ou atualize os dados
                    await PatchDataToAppAsync(data, 12345, appServer, appTokenAuth); // Exemplo de URL de um item qualquer
                }
                else
                {
                    Console.WriteLine($"Request failed with status code: {response.StatusCode}");
                }
            }
        }

        static async Task PostDataToAppAsync(string dataParameters, string appServer, string appTokenAuth)
        {
            HttpClient client = new HttpClient();

            string url = appServer;

            // Defina os dados a serem enviados no corpo da solicitação (se aplicável)
            var content = new StringContent(dataParameters);
            content.Headers.ContentType = new MediaTypeHeaderValue("application/json");

            // Defina os cabeçalhos da solicitação (se necessário)
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", appTokenAuth);

            HttpResponseMessage response = await client.PostAsync(url, content);

            if (response.IsSuccessStatusCode)
            {
                string responseData = await response.Content.ReadAsStringAsync(); // Supondo que a resposta está em formato JSON
                Console.WriteLine(responseData); // Imprima no terminal para demonstrar que a solicitação foi bem-sucedida e quais dados foram enviados
            }
            else
            {
                Console.WriteLine($"A solicitação falhou com o código de status {response.StatusCode}");
            }
        }

        static async Task PatchDataToAppAsync(string newValues, int itemUrl, string appServer, string appTokenAuth)
        {
            HttpClient client = new HttpClient();

            string url = $"{appServer}/{itemUrl}"; // Substitua pela URL real que você deseja usar

            // Defina os dados a serem enviados no corpo da solicitação (as atualizações que deseja fazer)
            var content = new StringContent(newValues);
            content.Headers.ContentType = new MediaTypeHeaderValue("application/json-patch+json");

            // Defina os cabeçalhos da solicitação (se necessário)
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", appTokenAuth);

            HttpResponseMessage response = await client.PatchAsync(url, content);

            if (response.IsSuccessStatusCode)
            {
                string responseData = await response.Content.ReadAsStringAsync(); // Supondo que a resposta está em formato JSON
                Console.WriteLine(responseData); // Imprima no terminal para demonstrar que a atualização foi bem-sucedida
            }
            else
            {
                Console.WriteLine($"A solicitação PATCH falhou com o código de status {response.StatusCode}");
            }
        }
    }
}
