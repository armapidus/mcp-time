from mcp.server import Server
from mcp.transport.stdio import StdioServerTransport
from zoneinfo import ZoneInfo
import datetime
import asyncio

server = Server(name="mcp-time", version="0.1.0")

@server.tool()
async def now(locale: str = "fr-FR", timeZone: str = "Europe/Paris") -> dict:
    """Retourne l'heure actuelle en ISO et formatée."""
    tz = ZoneInfo(timeZone)
    now = datetime.datetime.now(tz)
    return {
        "iso": now.isoformat(),
        "formatted": now.strftime("%c"),
        "epochMs": int(now.timestamp() * 1000),
        "timeZone": str(now.tzinfo)
    }

async def main():
    transport = StdioServerTransport()
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
