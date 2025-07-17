import { Box, Card, Divider, Group, Title } from "@mantine/core";

export function meta() {
	return [{ title: "Actions | JIVAS Manager" }];
}

export default function ChatRoute() {
	const host = localStorage.getItem("jivas-host");
	const token = localStorage.getItem("jivas-token");

	return (
		<Box py="xl" px="xl">
			<Group justify="space-between">
				<Title order={3}>Graph</Title>
			</Group>

			<Divider mt="xs" mb="xl" />

			<Card px="xl" h="80vh" withBorder>
				<iframe
					className="min-h-[740px]"
					title={"Action Config"}
					src={`${
						host?.includes("jivas")
							? host?.replace("jivas", "jvstudio")
							: "http://localhost:8501"
					}/?token=${token}`}
					width={"100%"}
					height={"100%"}
					style={{ border: "none", outline: "none" }}
					// className="w-full h-full bg-[red]"
				/>
			</Card>
		</Box>
	);
}
