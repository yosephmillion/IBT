import Menu from "./Menu/Menu";
import SideBar from "./SideBar/SideBar";

function Main() {
    return (
        <main
            style={{
                display: "grid",
                gridTemplateColumns: "240px 1fr",
                gap: "30px",
                padding: "30px",
                width: "100%",
                boxSizing: "border-box",
                alignItems: "start"
            }}
        >
            <SideBar />
            <Menu />
        </main>
    );
}

export default Main;