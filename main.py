import discord
import csv

from creds import creds

class OverlapClient(discord.Client):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.csv_file_name = "out/users.csv"
    self.my_servers = []
    self.my_users = {}
  async def on_ready(self):
    for server in self.servers:
      self.my_servers.append(server.name)
      for user in server.members:
        self.add_user_entry(user, server.name)
    self.write_csv()
    await self.logout()
  def add_user_entry(self, user, server):
    entry = self.my_users.get(user.id, {"name": user.name, "servers": []})
    entry["servers"].append(server)
    self.my_users[user.id] = entry
  def write_csv(self):
    with open(self.csv_file_name, 'w') as csv_file:
      csv_writer = csv.writer(csv_file)
      csv_writer.writerow(["ID", "Name"] + self.my_servers)
      for id, user in self.my_users.items():
        csv_writer.writerow(self.make_user_line(id, user))
  def make_user_line(self, id, user):
    line = [id, user["name"]]
    for server in self.my_servers:
      line.append(server in user["servers"])
    return line

if __name__ == "__main__":
  overlap_client = OverlapClient()
  overlap_client.run(*creds)
